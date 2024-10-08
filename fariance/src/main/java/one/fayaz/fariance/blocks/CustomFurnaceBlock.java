package one.fayaz.fariance.blocks;

import net.minecraft.world.InteractionHand;
import net.minecraft.world.InteractionResult;
import net.minecraft.world.MenuProvider;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.level.Level;
import net.minecraft.world.level.block.FurnaceBlock;
import net.minecraft.world.level.block.RenderShape;
import net.minecraft.world.level.block.entity.BlockEntity;
import net.minecraft.world.level.block.state.BlockBehaviour;

import net.minecraft.core.BlockPos;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.level.block.entity.BlockEntityType;
import net.minecraft.world.phys.BlockHitResult;
import net.minecraftforge.registries.RegistryObject;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraftforge.fml.javafmlmod.FMLJavaModLoadingContext;
import one.fayaz.fariance.FarianceMod;
import one.fayaz.fariance.ItemRegistry;

public class CustomFurnaceBlock extends FurnaceBlock {
    public static final DeferredRegister<BlockEntityType<?>> BLOCK_ENTITIES = DeferredRegister.create(ForgeRegistries.BLOCK_ENTITY_TYPES, FarianceMod.MODID);

    public static RegistryObject<BlockEntityType<CustomFurnaceBlockEntity>> CUSTOM_FURNACE_BLOCK_ENTITY;

    public CustomFurnaceBlock(BlockBehaviour.Properties properties) {
        super(properties);
    }


    public InteractionResult use(BlockState state, Level level, BlockPos pos, Player player, InteractionHand hand, BlockHitResult hit) {
        if (level.isClientSide) {
            return InteractionResult.SUCCESS;
        } else {
            this.openContainer(level, pos, player);
            return InteractionResult.CONSUME;
        }
    }

    @Override
    public BlockEntity newBlockEntity(BlockPos pos, BlockState state) {
        return new CustomFurnaceBlockEntity(pos, state);
    }

    @Override
    protected void openContainer(Level level, BlockPos pos, Player player) {
        BlockEntity blockEntity = level.getBlockEntity(pos);
        if (blockEntity instanceof CustomFurnaceBlockEntity) {
            player.openMenu((MenuProvider) blockEntity);
        }
    }

    @Override
    public RenderShape getRenderShape(BlockState state) {
        return RenderShape.MODEL;
    }

    public static void registerBlockEntities() {
        CUSTOM_FURNACE_BLOCK_ENTITY = BLOCK_ENTITIES.register(
                "custom_furnace",
                () -> BlockEntityType.Builder.of(CustomFurnaceBlockEntity::new,
                        ItemRegistry.GENERATED_BLOCKS.values().stream()
                                .filter(block -> block.get() instanceof CustomFurnaceBlock)
                                .map(RegistryObject::get)
                                .toArray(CustomFurnaceBlock[]::new)
                ).build(null)
        );

        BLOCK_ENTITIES.register(FMLJavaModLoadingContext.get().getModEventBus());
    }
}

class CustomFurnaceBlockEntity extends BlockEntity {
    public CustomFurnaceBlockEntity(BlockPos pos, BlockState state) {
        super(CustomFurnaceBlock.CUSTOM_FURNACE_BLOCK_ENTITY.get(), pos, state);
    }
}
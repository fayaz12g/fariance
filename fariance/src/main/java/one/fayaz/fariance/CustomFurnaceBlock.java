package one.fayaz.fariance;

import net.minecraft.world.level.block.FurnaceBlock;
import net.minecraft.world.level.block.RenderShape;
import net.minecraft.world.level.block.entity.BlockEntity;
import net.minecraft.world.level.block.state.BlockBehaviour;

import net.minecraft.core.BlockPos;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.level.block.entity.BlockEntityType;
import net.minecraftforge.registries.RegistryObject;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraftforge.fml.javafmlmod.FMLJavaModLoadingContext;

public class CustomFurnaceBlock extends FurnaceBlock {
    public static final DeferredRegister<BlockEntityType<?>> BLOCK_ENTITIES = DeferredRegister.create(ForgeRegistries.BLOCK_ENTITY_TYPES, FarianceMod.MODID);

    public static RegistryObject<BlockEntityType<CustomFurnaceBlockEntity>> CUSTOM_FURNACE_BLOCK_ENTITY;

    public CustomFurnaceBlock(BlockBehaviour.Properties properties) {
        super(properties);
    }

    @Override
    public BlockEntity newBlockEntity(BlockPos pos, BlockState state) {
        return new CustomFurnaceBlockEntity(pos, state);
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
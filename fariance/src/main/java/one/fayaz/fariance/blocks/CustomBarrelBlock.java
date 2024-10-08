package one.fayaz.fariance.blocks;

import net.minecraft.core.BlockPos;
import net.minecraft.core.Direction;
import net.minecraft.core.NonNullList;
import net.minecraft.world.Container;
import net.minecraft.world.ContainerHelper;
import net.minecraft.world.WorldlyContainer;
import net.minecraft.world.entity.player.Player;
import net.minecraft.world.item.ItemStack;
import net.minecraft.world.level.block.Block;
import net.minecraft.world.level.block.EntityBlock;
import net.minecraft.world.level.block.entity.BlockEntity;
import net.minecraft.world.level.block.entity.BlockEntityType;
import net.minecraft.world.level.block.state.BlockBehaviour;
import net.minecraft.world.level.block.state.BlockState;
import net.minecraft.world.level.block.state.StateDefinition;
import net.minecraft.world.level.block.state.properties.BlockStateProperties;
import net.minecraft.world.level.block.state.properties.BooleanProperty;
import net.minecraft.world.level.block.state.properties.DirectionProperty;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.ForgeRegistries;
import net.minecraftforge.registries.RegistryObject;
import net.minecraftforge.fml.javafmlmod.FMLJavaModLoadingContext;
import one.fayaz.fariance.FarianceMod;
import one.fayaz.fariance.ItemRegistry;

import javax.annotation.Nullable;

public class CustomBarrelBlock extends Block implements EntityBlock {
    public static final DirectionProperty FACING = BlockStateProperties.FACING;
    public static final BooleanProperty OPEN = BlockStateProperties.OPEN;

    public static final DeferredRegister<BlockEntityType<?>> BLOCK_ENTITIES = DeferredRegister.create(ForgeRegistries.BLOCK_ENTITY_TYPES, FarianceMod.MODID);

    public static RegistryObject<BlockEntityType<CustomBarrelBlockEntity>> CUSTOM_BARREL_BLOCK_ENTITY;

    public CustomBarrelBlock(BlockBehaviour.Properties properties) {
        super(properties);
        this.registerDefaultState(this.stateDefinition.any().setValue(FACING, Direction.NORTH).setValue(OPEN, Boolean.FALSE));
    }

    @Override
    protected void createBlockStateDefinition(StateDefinition.Builder<Block, BlockState> builder) {
        builder.add(FACING, OPEN);
    }

    @Nullable
    @Override
    public BlockEntity newBlockEntity(BlockPos pos, BlockState state) {
        return new CustomBarrelBlockEntity(pos, state);
    }

    public static void registerBlockEntities() {
        CUSTOM_BARREL_BLOCK_ENTITY = BLOCK_ENTITIES.register(
                "custom_barrel",
                () -> BlockEntityType.Builder.of(CustomBarrelBlockEntity::new,
                        ItemRegistry.GENERATED_BLOCKS.values().stream()
                                .filter(block -> block.get() instanceof CustomBarrelBlock)
                                .map(RegistryObject::get)
                                .toArray(CustomBarrelBlock[]::new)
                ).build(null)
        );

        BLOCK_ENTITIES.register(FMLJavaModLoadingContext.get().getModEventBus());
    }

    // Add other necessary methods like use, onRemove, etc.
}

class CustomBarrelBlockEntity extends BlockEntity implements WorldlyContainer {
    private NonNullList<ItemStack> items = NonNullList.withSize(27, ItemStack.EMPTY);

    public CustomBarrelBlockEntity(BlockPos pos, BlockState state) {
        super(CustomBarrelBlock.CUSTOM_BARREL_BLOCK_ENTITY.get(), pos, state);
    }

    @Override
    public int[] getSlotsForFace(Direction side) {
        return new int[27]; // Allow access from all sides
    }

    @Override
    public boolean canPlaceItemThroughFace(int index, ItemStack itemStackIn, @Nullable Direction direction) {
        return true; // Allow placing items from all sides
    }

    @Override
    public boolean canTakeItemThroughFace(int index, ItemStack stack, Direction direction) {
        return true; // Allow taking items from all sides
    }

    @Override
    public int getContainerSize() {
        return 27;
    }

    @Override
    public boolean isEmpty() {
        return this.items.stream().allMatch(ItemStack::isEmpty);
    }

    @Override
    public ItemStack getItem(int index) {
        return this.items.get(index);
    }

    @Override
    public ItemStack removeItem(int index, int count) {
        return ContainerHelper.removeItem(this.items, index, count);
    }

    @Override
    public ItemStack removeItemNoUpdate(int index) {
        return ContainerHelper.takeItem(this.items, index);
    }

    @Override
    public void setItem(int index, ItemStack stack) {
        this.items.set(index, stack);
        if (stack.getCount() > this.getMaxStackSize()) {
            stack.setCount(this.getMaxStackSize());
        }
    }

    @Override
    public boolean stillValid(Player player) {
        return Container.stillValidBlockEntity(this, player);
    }

    @Override
    public void clearContent() {
        this.items.clear();
    }

    // Add methods for saving and loading NBT data
}